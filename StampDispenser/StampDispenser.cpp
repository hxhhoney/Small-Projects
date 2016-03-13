#include <stdlib.h>
#include <assert.h>
#include<algorithm>
#include<vector>
using namespace std;
/// <summary>
/// Facilitates dispensing stamps for a postage stamp machine.
/// </summary>
class StampDispenser
{
public:
    /// <summary>
    /// Initializes a new instance of the <see cref="StampDispenser"/> class that will be 
    /// able to dispense the given types of stamps.
   
    /// </summary>
    /// <param name="stampDenominations">
    /// The values of the types of stamps that the machine has.
    /// Should be sorted in descending order and contain at least a 1.
    /// </param>
    const int *stampDenominations;
    
    /// <param name="numStampDenominations">
    /// The number of types of stamps in the stampDenominations array. 
    /// </param>
    size_t numStampDenominations=1;
    StampDispenser(const int* stampDenominations, size_t numStampDenominations)
    {
        this->numStampDenominations=numStampDenominations;
        this->stampDenominations=stampDenominations;
    };
    
    /// <summary>
    /// Returns the minimum number of stamps that the machine can dispense to
    /// fill the given request.
    
    /// </summary>
    /// <param name="request">
    /// The total value of the stamps to be dispensed.
    /// </param>
    
    /// <returns>
    /// The minimum number of stamps needed to fill the given request.
    /// </returns>
    int CalcNumStampsToFillRequest(int request)
    {
        //I use DP to do it.
        //dp[i]=d[i-stamp]+1;
        vector<int> dp(request+1,INT_MAX);//dp[i] is the min number of stamps to meet value i;
        dp[0]=0;
        for(int j=int(numStampDenominations-1);j>=0;j--)
        {
            for(int i=stampDenominations[j];i<=request;i++)
            {
                if(dp[i-stampDenominations[j]]!=INT_MAX)
                {
                    dp[i]=min(dp[i-stampDenominations[j]]+1,dp[i]);
                }
            }
        }
        return dp[request]==INT_MAX?-1:dp[request];
        
    };
}; 

int main()
{
    ////int stampDenominations[] = {90, 30, 24, 10, 6, 2, 1};
    ////StampDispenser stampDispenser(stampDenominations, 7);
    ////assert(stampDispenser.CalcNumStampsToFillRequest(18) == 3);

    return 0;
}
