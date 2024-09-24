package exercice;

import java.time.LocalDate;
import java.time.Period;

public class Employe extends Personne {
	
	private double salaireEmploye; 
	private final LocalDate dateEmbauche;
	public static final int AGE_MINIMUM = 16;
	public static final int AGE_MAXIMUM = 65;

	
	
	protected Employe (String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate laDateEmbauche) {
		super(leNom, lePrenom,laDate, lAdresse);
		salaireEmploye = leSalaire;
		dateEmbauche = laDateEmbauche;
	}
	
	public static Employe createEmploye(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, double leSalaire, LocalDate laDateEmbauche) {
	    LocalDate now = LocalDate.now();
	    int age = Period.between(laDate, now).getYears(); 

	    if (age >= AGE_MINIMUM && age < AGE_MAXIMUM) {
          
	    	return new Employe(leNom, lePrenom, laDate, lAdresse, leSalaire, laDateEmbauche);

	    } else {
            System.err.println("L'âge de la personne doit être entre "+AGE_MINIMUM +" et "+AGE_MAXIMUM+" ans.");
            return null; 
        }
		
		
	}
	
	 public void augmenterLeSalaire(double pourcentage) {
	        if (pourcentage > 0) {
	            salaireEmploye += salaireEmploye * (pourcentage / 100);
	            System.out.println("Le salaire a été augmenté de " + pourcentage + "%.");
	        } else {
	            System.err.println("Le pourcentage doit être positif !");
	        }
	 }
	 
	 public int calculerAnnuite() {
	        LocalDate today = LocalDate.now(); 
	        Period period = Period.between(dateEmbauche, today);  //period = P(nbrJour)D(nbrMois)M(nbrAnne)A  
	        int annuite = period.getYears(); 

	        // Si l'année en cours est entamée, on compte comme une année complète
	        if (period.getMonths() > 0 || period.getDays() > 0) {
	            annuite++;
	        }

	        return annuite;
	 }

	public double getSalaireEmploye() {
		return salaireEmploye;
	}

	public void setSalaireEmploye(double salaireEmploye) {
		this.salaireEmploye = salaireEmploye;
	}

	public LocalDate getDateEmbauche() {
		return dateEmbauche;
	}

	@Override
	public String toString() {
		return "Employe [salaireEmploye=" + salaireEmploye + ", dateEmbauche=" + dateEmbauche + "]";
	}
	
	
	
}
