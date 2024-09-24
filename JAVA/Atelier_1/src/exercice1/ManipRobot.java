package exercice1;

public class ManipRobot {

    public static void main(String[] args) {
        Robot monBotToni = new Robot("Toto", 10, 20, Robot.SUD);
        
        Robot monBotLola = new Robot("Titi", 0, 0, Robot.NORD);
        
        System.out.println("Position initiale de Toto : (" + monBotToni.getX() + ", " + monBotToni.getY() + ") direction " + monBotToni.getOrientation());
        System.out.println("Position initiale de Titi : (" + monBotLola.getX() + ", " + monBotLola.getY() + ") direction " + monBotLola.getOrientation());
        
        monBotToni.moveBot();
        System.out.println("Après déplacement, position de Toto : (" + monBotToni.getX() + ", " + monBotToni.getY() + ") direction " + monBotToni.getOrientation());
        
        monBotToni.setOrientationRobot(Robot.EST);
        System.out.println("Toto change de direction vers " + monBotToni.getOrientation());
        
        monBotToni.moveBot();
        System.out.println("Après déplacement, position de Toto : (" + monBotToni.getX() + ", " + monBotToni.getY() + ") direction " + monBotToni.getOrientation());
        
        monBotLola.moveBot();
        System.out.println("Après déplacement, position de Titi : (" + monBotLola.getX() + ", " + monBotLola.getY() + ") direction " + monBotLola.getOrientation());
        
        monBotLola.setOrientationRobot(Robot.OUEST);
        System.out.println("Titi change de direction vers " + monBotLola.getOrientation());
        
        monBotLola.moveBot();
        System.out.println("Après déplacement, position de Titi : (" + monBotLola.getX() + ", " + monBotLola.getY() + ") direction " + monBotLola.getOrientation());
    }
}
