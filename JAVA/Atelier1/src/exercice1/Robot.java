package exercice1;

public class Robot {
	
	private String refBot;
	private String nameBot;
	private int x;
	private int y;
	private int directionBot;
	private static int numberBot = 1;
	
	private static final int NORD = 1;
	private static final int SUD = 2;
	private static final int EST = 3;
	private static final int OUEST = 4;

	
	public Robot(String nameBot ,int x ,int y, int directionBot  ){
		this.refBot = "ROB"+ numberBot;
		this.nameBot = nameBot;
		this.x = x;
		this.y = y;
		this.directionBot = directionBot;
		
		numberBot++ ;		
		
	}
	
	
	public Robot(String nameBot){
		this.refBot = "ROB"+ numberBot;
		this.nameBot = nameBot;
		this.x = 0;
		this.y = 0;
		this.directionBot = 1;
		
		numberBot++ ;		
		
	}
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub	
		  
	}

	public void setOrientationRobot(int newBotOrientation) {
		
		directionBot = newBotOrientation;
		
		
	}
	
	public void moveBot() {
		
		
		
		
	}

	
	
}



