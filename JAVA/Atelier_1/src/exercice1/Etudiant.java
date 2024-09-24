package exercice1;

public class Etudiant extends Personne {
	
	private final String  numEtu;
	
	
	 // Constructeur de la classe Etudiant qui appelle le constructeur de la classe Personne
    public Etudiant(String nom, int age, String numEtu) {
        super(nom, age); // Appel du constructeur de la classe Personne
        this.numEtu = numEtu;
    }
	
	
	
	public String getNumEtu() {
		return this.numEtu;
	}

	@Override
	public String toString() {
		return "Etudiant [numEtu=" + numEtu + "]";
	}



}
