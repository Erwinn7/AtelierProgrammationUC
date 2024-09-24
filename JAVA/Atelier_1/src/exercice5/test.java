package exercice5;

public class test {
	
	public static void main(String[] args) {
        Universite universite = new Universite("UNIVERSITE DE CORSE");

        Enseignant titulaire1 = new Titulaire("Pierre", 1500.0);    // le nom et le salaire du titulaire 
        Enseignant titulaire2 = new Titulaire("Laurent", 2500.0);
        Enseignant vacataire1 = new Vacataire("Michel", 15);  // le nom et le nombre d'heure que fait le  du vacataire 
        Enseignant vacataire2 = new Vacataire("Marie", 60);  
        universite.embaucher(titulaire1);
        universite.embaucher(titulaire2);
        universite.embaucher(vacataire1);
        universite.embaucher(vacataire2);

        universite.afficherSalaires();
    }

}
