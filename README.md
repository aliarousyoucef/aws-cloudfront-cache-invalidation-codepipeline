**AWS CloudFront Cache Invalidation**

This is a small function that can be invoked to invalidate the cache of a CloudFront Distribution.

Updated slightly from the aws-cloudfront-cache-invalidation script to send a response to CodePipeline on success.

The purpose of this function is to be called as required as a standalone function when you need your cache invalidated and the functionality is not in-built to the tool or service you are using.
**Example**: This function is called during the Deploy stage of a CodePipeline to invalidate the cache of a CloudFront Distribution for a static website hosted in Amazon S3

**How to use**
1. Create a new **Lambda** function
2. Select **Python 3.8** as the runtime
3. Copy the source code into your function
4. Create execution role and assign permissions to your cloudfront distribution
5. Create an User parameters in your CodePipeline action with distribution value
6. Deploy function


**Note**
This function invalidates the entire cache. To select paths update the **items* sections within the function
