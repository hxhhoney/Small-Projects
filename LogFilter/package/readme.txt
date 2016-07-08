Created by Cathy Huang.
ToolName: LogFilter

(1)Function Explanation:
When we do a series of actions on a HU, the correlated logs will be 
generated on different servers based on load balancer. To have a clear view on the request-response information, we need to do two things. 
1.Search for required information and shield unnecessary lines.
2. Merge required logs, which are allocated to different servers ,into one continuously log in an order of timestamp. 
This tool help obtain the final merged log.

(2)Steps to run.
1. Create a file called package.

2.Under package, create a file called origin. Put bento1,bento2,….into origin.(This is the file for input, and each bento file collects all logs from one server. The file names should strictly be the same as I mentioned above).

2. Create a file called input. Put it in package.

3.Put parameters.properties in package.

4.Put LogTool.jar in package.

5.Go to package, run command java -jar LogTool.jar

6. finaloutput.txt generated in the same directory as package.

(3)Change profileId:
open parameters.properties, change the value of profileId to the one you want.
Then the tool will only search for the requests and response with the new profileId.