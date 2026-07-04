class Solution
{
    public int[] twoSum(int[] numbers, int target)
    {
        int left = 0, right = numbers.length-1, max=0;
        while(left<right){
            max = numbers[left]+numbers[right];
            if(max==target){
                return new int[]{left+1,right+1};
            }
            else{
                if(max<target) left++;
                else right--;
            }
        }
        return new int []{left+1,right+1};
    }
}
