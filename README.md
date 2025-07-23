# awsbilling

Policy required for `addtags` function:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSnapshots",
                "ec2:DescribeVolumes",
                "ec2:DescribeImages",
                "ec2:DescribeInstances",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeAddresses",
                "ec2:CreateTags"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:ListAliases",
                "kms:ListResourceTags",
                "kms:TagResource"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "route53:ListHostedZones",
                "route53:ListTagsForResource",
                "route53:ChangeTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

Policy required for `costs` function:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ce:GetCostAndUsage",
                "ce:GetCostAndUsageWithResources",
                "ce:GetCostForecast",
                "ce:GetDimensionValues",
                "ce:GetReservationCoverage",
                "ce:GetReservationPurchaseRecommendation",
                "ce:GetReservationUtilization",
                "ce:GetRightsizingRecommendation",
                "ce:GetSavingsPlansCoverage",
                "ce:GetSavingsPlansPurchaseRecommendation",
                "ce:GetSavingsPlansUtilization",
                "ce:GetTags",
                "ce:GetUsageForecast"
            ],
            "Resource": "*"
        }
    ]
}
```

Policy required to call Lambda functions externally:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:ListFunctions",
                "lambda:GetFunction",
                "lambda:GetAccountSettings",
                "lambda:ListTags"
            ],
            "Resource": "*"
        }
    ]
}
```

<!-- footer -->
as
as
