package java_lang;

class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int[] daysInMonth = {0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        int arriveAliceDate = daysInMonth[Integer.parseInt(arriveAlice.substring(0, 2)) - 1] + Integer.parseInt(arriveAlice.substring(3));
        int leaveAliceDate = daysInMonth[Integer.parseInt(leaveAlice.substring(0, 2)) - 1] + Integer.parseInt(leaveAlice.substring(3));
        int arriveBobDate = daysInMonth[Integer.parseInt(arriveBob.substring(0, 2)) - 1] + Integer.parseInt(arriveBob.substring(3));
        int leaveBobDate = daysInMonth[Integer.parseInt(leaveBob.substring(0, 2)) - 1] + Integer.parseInt(leaveBob.substring(3));

        if (leaveAliceDate < arriveBobDate || leaveBobDate < arriveAliceDate) {
            return 0;
        } else if ((arriveAliceDate < arriveBobDate && leaveAliceDate > leaveBobDate) || (arriveAliceDate > arriveBobDate && leaveAliceDate < leaveBobDate)) {
            return Math.min(leaveAliceDate - arriveAliceDate, leaveBobDate - arriveBobDate) + 1;
        } else {
            return Math.min(leaveAliceDate - arriveBobDate, leaveBobDate - arriveAliceDate) + 1;
        }
    }
}

public class Problem2409 {
    public static void main(String[] args) {
        String arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19";
        var solution = new Solution();
        System.out.println(solution.countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob));
    }
}
