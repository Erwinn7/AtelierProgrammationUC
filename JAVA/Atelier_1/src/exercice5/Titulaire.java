package exercice5;

public class Titulaire extends Enseignant{
	
	private double salaire ;
	
	public Titulaire (String nameTitulaire, double salaireTitulaire) {
		super(nameTitulaire);
		this.salaire = salaireTitulaire;
	}

	
	@Override
	public double salaire() {
		return this.salaire;
	}


	@Override
	public String toString() {
		return super.toString() +" (Titulaire) : " + salaire + " euros";
	}

}
