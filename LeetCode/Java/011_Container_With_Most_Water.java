class Solution {
    public int maxArea(int[] height) {
        int left=0, right=height.length-1;
        int n = height.length;
        int max=0, current=max;
        while(left<right){
            int width = right - left;
            current=Math.min(height[left],height[right])*width;
            max = Math.max(current,max);
            if(height[left]<height[right])
                left++;
            else
                right--;
        }
        return max;
    }
}