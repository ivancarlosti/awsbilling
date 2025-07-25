import boto3
import datetime

def generate_bind_zone_file(domain_name, records):
    """
    Generates a simplified BIND zone file as a string.
    """
    output = []
    output.append(f"$TTL 300")
    output.append(f"@  IN  SOA ns-123.awsdns-45.com. awsdns-hostmaster.amazon.com. (")
    output.append(f"    {datetime.datetime.utcnow().strftime('%Y%m%d%H')} ; serial")
    output.append(f"    7200     ; refresh")
    output.append(f"    900      ; retry")
    output.append(f"    1209600  ; expire")
    output.append(f"    86400 )  ; minimum")

    output.append(f"@  IN  NS  ns-123.awsdns-45.com.")
    output.append("")

    for record in records:
        record_name = record['Name'].rstrip('.')
        record_type = record['Type']
        ttl = record.get('TTL', 300)
        values = record.get('ResourceRecords', [])
        if record_type in ['SOA', 'NS'] and record_name == domain_name:
            continue  # already handled above

        for val in values:
            val_str = val['Value']
            output.append(f"{record_name} {ttl} IN {record_type} {val_str}")

    return "\n".join(output)

def lambda_handler(event, context):
    client = boto3.client('route53')
    response = client.list_hosted_zones()
    zones = response['HostedZones']

    output = []

    for zone in zones:
        zone_id = zone['Id'].split("/")[-1]
        domain_name = zone['Name'].rstrip('.')

        records_response = client.list_resource_record_sets(HostedZoneId=zone_id)
        records = records_response['ResourceRecordSets']

        bind_file = generate_bind_zone_file(domain_name, records)

        output.append({
            "domain": domain_name,
            "bind_file": bind_file
        })

    return {
        "statusCode": 200,
        "zones": output
    }
