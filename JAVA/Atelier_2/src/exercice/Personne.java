package exercice;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Objects;

public class Personne implements Cloneable{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    public final LocalDate dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
    private static int nbPersonnes;
    
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		
		nbPersonnes += 1;
	}
	

	 
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'année de naissance
	 * @param numero le numero de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, LocalDate.of(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	
	public static boolean plusAgee(Personne firstPerson , Personne secondPerson) {
		if (firstPerson == null || secondPerson == null) {
            System.err.println("Erreur : La personne à comparer est n'existe pas.");
            return false;
        }
		
	   return firstPerson.getDateNaissance().isBefore(secondPerson.getDateNaissance());
		
	}
	
	
	
	public boolean plusAgeeQue(Personne secondPerson) {
		if (secondPerson == null) {
            System.err.println("Erreur : La personne à comparer est n'existe pas.");
            return false;
        }
	    return this.dateNaissance.isBefore(secondPerson.getDateNaissance());
	    
	}
	
	public boolean plusAgeeQue3(Personne secondPerson) {
		
	    return Personne.plusAgee(this, secondPerson);
	    
	}
	
	@Override
	public boolean equals(Object obj) {
	    if (obj == null && obj instanceof Personne) return false; 

	    Personne secondPerson = (Personne) obj; 

	    // on utilse  Objects.equals pour comparer les valeurs des variables et non leur adresses mémoires
	    return Objects.equals(this.nom, secondPerson.nom)
	        && Objects.equals(this.prenom, secondPerson.prenom)
	        && Objects.equals(this.dateNaissance, secondPerson.dateNaissance);
	    
	}


	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le prénom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance
	 */
	public LocalDate getDateNaissance(){
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}
	
	public static int getNbPersonne() {
		return nbPersonnes;
	}
		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.format(DateTimeFormatter.ofPattern("dd-MM-yyyy"))+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}
	
  
 
 }

    
   
   