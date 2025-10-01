// There are numBottles water bottles that are initially full of water. 
// You can exchange numExchange empty water bottles from the market with one full water bottle.

// The operation of drinking a full water bottle turns it into an empty bottle.

// Given the two integers numBottles and numExchange, 
// return the maximum number of water bottles you can drink

class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int drinked = numBottles;
        int empty_bottles = 0;
        while (numBottles >= numExchange){
            drinked = drinked + ( numBottles / numExchange);
            empty_bottles = numBottles / numExchange;
            numBottles = (numBottles % numExchange) + empty_bottles;
        }
        return drinked;
    }

    public static void main(String[] args) {
      Solution sol = new Solution();
      int numBottles = 15;
      int numExchange = 4;
      System.out.println("Number of water bottles you can drink: " + sol.numWaterBottles(numBottles, numExchange));
    }


}


