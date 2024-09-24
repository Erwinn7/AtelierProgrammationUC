package exercice;

import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;

public class Secretaire extends Employe {
	
	public final int NBTOTALCHEF = 5;
	private ArrayList<Manager> listDesChefs ;
	
	

	protected Secretaire(String leNom, String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire,
			LocalDate laDateEmbauche) {
		super(leNom, lePrenom, laDate, lAdresse, leSalaire, laDateEmbauche);
	}
	
	public static Secretaire createEmploye(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate laDateEmbauche) {
	    LocalDate now = LocalDate.now();
	    int age = Period.between(laDate, now).getYears(); 

	    if (age >= 16 && age < 65) {
          
	    	return new Secretaire(leNom, lePrenom, laDate, lAdresse, leSalaire, laDateEmbauche);

	    } else {
            System.err.println("L'âge de la personne doit être entre 16 et 65 ans.");
            return null; 
        }
		
		
	}
	
	
	@Override
    public void augmenterLeSalaire(double pourcentage) {
        if (pourcentage > 0) {

            double bonus = listDesChefs.size() * 0.1; 

            // On applique l'augmentation de salaire avec le bonus
            double pourcentageAugTot = pourcentage + bonus;
            this.setSalaireEmploye(this.getSalaireEmploye()*(pourcentageAugTot / 100));

            System.out.println("Le salaire a été augmenté de " + pourcentage + "% avec un bonus de " + bonus + "% pour l'ancienneté.");
        } else {
            System.err.println("Le pourcentage doit être positif !");
        }
    }
	
	
	
	
	
	

	public ArrayList<Manager> getListDesChefs() {
		return listDesChefs;
	}

	public void setListDesChefs(Manager leNouveauChef) {
		
		if (this.listDesChefs.size()  <= NBTOTALCHEF ) {
			this.listDesChefs.add(leNouveauChef);
		}
	}
	
	
	
	
	
	
	

}
