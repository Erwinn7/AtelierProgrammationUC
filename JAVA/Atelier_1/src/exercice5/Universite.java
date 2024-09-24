package exercice5;

import java.util.ArrayList;

public class Universite {
	private String nom;
	private ArrayList<Enseignant> listeEnseignants ;
	
	public Universite (String nom) {
		this.nom = nom ;
		this.listeEnseignants = new ArrayList<Enseignant>() ;
	}
	
    public void afficherSalaires() {
    	double totalSalaire =0 ;
        System.out.println("Liste des enseignants de l'université " + nom );
        for (Enseignant enseignant : listeEnseignants) {
            System.out.println(enseignant);
            totalSalaire += enseignant.salaire()  ;
        }
        System.out.println("Total des salaires versé : " + totalSalaire + " euros");

    }
	
   public void embaucher(Enseignant e) {
        this.listeEnseignants.add(e);
   }

	
	
	
}
