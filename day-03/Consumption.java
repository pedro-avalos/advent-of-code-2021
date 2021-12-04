import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Consumption.
 * 
 * @author Pedro Avalos
 */
public class Consumption {

  public static void main(String[] args) {
    String name = args.length > 0 ? args[0] : "input.txt";
    File file = new File(name);
    Scanner scanner = null;

    try {
      scanner = new Scanner(file);
    } catch (FileNotFoundException e) {
      System.out.println("File '" + name + "' not found.");
      e.printStackTrace();
      System.exit(1);
    }

    ArrayList<String> report = new ArrayList<>();
    while (scanner.hasNextLine())
      report.add(scanner.nextLine().strip());
    scanner.close();

    int length = report.get(0).length();
    String gammaBits = "";
    String epsilonBits = "";
    for (int i = 0; i < length; i++) {
      int countOnes = 0;

      for (String num : report) {
        try {
          countOnes += Integer.parseInt("" + num.charAt(i));
        } catch (NumberFormatException e) {
          System.out.println("Noninteger input.");
          e.printStackTrace();
          System.exit(1);
        }
      }

      gammaBits += (2 * countOnes >= report.size()) ? 1 : 0;
      epsilonBits += (2 * countOnes < report.size()) ? 1 : 0;
    }

    int gamma = Integer.parseInt(gammaBits, 2);
    int epsilon = Integer.parseInt(epsilonBits, 2);

    System.out.println("Part 1: " + (gamma * epsilon));

    ArrayList<String> generatorCandidates = new ArrayList<>(report);
    int i = 0;  // Position of char being considered
    while (generatorCandidates.size() > 1) {
      int countOnes = 0;
      for (String s : generatorCandidates)
        countOnes += Integer.parseInt("" + s.charAt(i));
      char majority = (2 * countOnes >= generatorCandidates.size()) ? '1' : '0';

      for (int j = 0; j < generatorCandidates.size(); j++)
        if (generatorCandidates.get(j).charAt(i) != majority)
          generatorCandidates.remove(j--);

      i++;
    }

    ArrayList<String> scrubberCandidates = new ArrayList<>(report);
    i = 0;  // Position of char being considered
    while (scrubberCandidates.size() > 1) {
      int countOnes = 0;
      for (String s : scrubberCandidates)
        countOnes += Integer.parseInt("" + s.charAt(i));
      char minority = (2 * countOnes < scrubberCandidates.size()) ? '1' : '0';

      for (int j = 0; j < scrubberCandidates.size(); j++)
        if (scrubberCandidates.get(j).charAt(i) != minority)
          scrubberCandidates.remove(j--);

      i++;
    }

    long generator = Integer.parseInt(generatorCandidates.get(0), 2);
    long scrubber = Integer.parseInt(scrubberCandidates.get(0), 2);

    System.out.println("Part 2: " + (generator * scrubber));
  }
}
