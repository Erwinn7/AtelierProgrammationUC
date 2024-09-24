package testatelier2;

import java.time.LocalDate;

import exercice.Adresse;
import exercice.Personne;

public class TestQuestion1 {

    public static void main(String[] args) {
        // Test de la création de personnes avec différentes méthodes de construction
        Personne personne1 = new Personne("Doe", "John", LocalDate.of(1990, 5, 15), new Adresse(1, "Rue de Paris", "75001", "Paris"));
        Personne personne2 = new Personne("Smith", "Alice", 25, 12, 1985, 10, "Avenue de Lyon", "69001", "Lyon");

        // Affichage des personnes créées
        System.out.println("Personne 1 : " + personne1);
        System.out.println("Personne 2 : " + personne2);

        // Test de la méthode equals
        System.out.println("\nTest de la méthode equals : ");
        Personne memePersonne1 = new Personne("Doe", "John", LocalDate.of(1990, 5, 15), new Adresse(1, "Rue de Paris", "75001", "Paris"));
        System.out.println("Personne 1 et Personne 1 (même objet) : " + personne1.equals(personne1)); // true
        System.out.println("Personne 1 et Même Personne 1 (objets différents mais mêmes attributs) : " + personne1.equals(memePersonne1)); // true
        System.out.println("Personne 1 et Personne 2 : " + personne1.equals(personne2)); // false

        // Test de la méthode plusAgee
        System.out.println("\nTest de la méthode plusAgee : ");
        System.out.println("Personne 1 est plus âgée que Personne 2 : " + Personne.plusAgee(personne1, personne2)); // false (personne2 est née avant personne1)

        // Test de la méthode plusAgeeQue
        System.out.println("\nTest de la méthode plusAgeeQue : ");
        System.out.println("Personne 1 est plus âgée que Personne 2 : " + personne1.plusAgeeQue(personne2)); // false (personne2 est née avant personne1)
    }
}
