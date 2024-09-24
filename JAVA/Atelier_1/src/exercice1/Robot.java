package exercice1;

public class Robot {
	
	private String refBot;
	private String nameBot;
	private int x;
	private int y;
	private int directionBot;
	private static int numberBot = 1;
	
	public  static final int NORD = 1;
	public  static final int SUD = 2;
	public  static final int EST = 3;
	public  static final int OUEST = 4;

	
	public Robot(String nameBot ,int x ,int y, int directionBot  ){
		this.refBot = "ROB"+ numberBot;
		this.nameBot = nameBot;
		this.x = x;
		this.y = y;
		this.directionBot = directionBot;
		
		numberBot++ ;		
		
	}
	
	
    public Robot(String nameBot) {
        this(nameBot, 0, 0, NORD);
    }
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub	
		  
	}

	public void setOrientationRobot(int newBotOrientation) {
//		Rajouter une vérification 
		directionBot = newBotOrientation;
		
		
	}
	
	// Méthode pour déplacer le robot
    public void moveBot() {
        switch (directionBot) {
            case NORD:
                y++;  
            break;
            case SUD:
                if (y > 0) {
                	y--;
                }else {
                	System.out.println("Vous ne pouvez vous déplacer hors du domaine");    
                }
                break;

            case EST:
                x++;  
                break;

            case OUEST:
                if (x > 0) {
                	x-- ;
                }else {
                	System.out.println("Vous ne pouvez vous déplacer hors du domaine");    
                }
                break; 
            default:
                System.out.println("Orientation invalide !");
        }
    }
    
    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String getOrientation() {
        switch (directionBot) {
            case NORD: return "Nord";
            case SUD: return "Sud";
            case EST: return "Est";
            case OUEST: return "Ouest";
            default: return "Inconnue";
    }

	
	
}


	public String toString() {
		return "Robot [refBot=" + refBot + ", nameBot=" + nameBot + ", x=" + x + ", y=" + y + ", directionBot="
				+ directionBot + "]";
	}

}



