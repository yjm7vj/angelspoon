public class Main{


    public static void main(String[] args){

        WildKingdom valley = new WildKingdom();

        if (args.length != 3){
            System.out.println("Sorry, I'm expecting three arguments.")
        }

        else {

            try {
                int numberOfWolves = Integer.parseInt(args[0]);

                int numberOfRabbits = Integer.parseInt(args[1]);

                int numberOfMonths = Integer.parseInt(args[2]);
            } catch (NumberFormatException e){

                System.out.println("I didn't understand one of your number");
                System.exit(0);
            }



            WildKingdom valley = new WildKingdom(numberOfWolves, numberOfRabbits, numberOfMonths);




        }

    }
}