package exercice5;

abstract class Enseignant  {
	
	protected String nameTeacher ;
	
	public Enseignant(String nameT) {
		this.nameTeacher = nameT;
		
	}
	
	public abstract double salaire();
	
	public String getNameTeacher() {
		return this.nameTeacher;
	}

	@Override
	public String toString() {
		return "Enseignant :" + nameTeacher ;
	}
	
}
