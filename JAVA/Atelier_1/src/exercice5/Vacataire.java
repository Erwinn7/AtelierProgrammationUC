package exercice5;

public class Vacataire extends Enseignant {
	
	public static final double VACATAIREREM = 40;
	private int nbHeuresCours;
	
	public Vacataire (String nameVacataire, int nbHeureCours){
		super(nameVacataire);
		this.nbHeuresCours = nbHeureCours; 
	}
	
	
	@Override
	public double salaire() {
		return this.nbHeuresCours*this.VACATAIREREM ;
	}


	@Override
	public String toString() {
		return nameTeacher+" (Vacataire "+ nbHeuresCours + " heures) : " + salaire() + " euros";
	}
	

}
