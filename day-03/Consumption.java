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

      for (String num : report)
        try {
          countOnes += Integer.parseInt("" + num.charAt(i));
        } catch (NumberFormatException e) {
          System.out.println("Noninteger input '" + num + "'.");
          System.exit(1);
        }

      gammaBits += (2 * countOnes >= report.size()) ? "1" : "0";
      epsilonBits += (2 * countOnes < report.size()) ? "1" : "0";
    }

    long gamma = Integer.parseInt(gammaBits, 2);
    long epsilon = Integer.parseInt(epsilonBits, 2);

    System.out.println("Part 1: " + (gamma * epsilon));

    ArrayList<String> generatorCandidates = new ArrayList<>(report);
    for (int charPos = 0; generatorCandidates.size() > 1; charPos++) {
      int countOnes = 0;
      for (String s : generatorCandidates)
        countOnes += Integer.parseInt("" + s.charAt(charPos));
      char majority = (2 * countOnes >= generatorCandidates.size()) ? '1' : '0';

      for (int j = 0; j < generatorCandidates.size(); j++)
        if (generatorCandidates.get(j).charAt(charPos) != majority)
          generatorCandidates.remove(j--);
    }

    ArrayList<String> scrubberCandidates = new ArrayList<>(report);
    for (int charPos = 0; scrubberCandidates.size() > 1; charPos++) {
      int countOnes = 0;
      for (String s : scrubberCandidates)
        countOnes += Integer.parseInt("" + s.charAt(charPos));
      char minority = (2 * countOnes < scrubberCandidates.size()) ? '1' : '0';

      for (int j = 0; j < scrubberCandidates.size(); j++)
        if (scrubberCandidates.get(j).charAt(charPos) != minority)
          scrubberCandidates.remove(j--);
    }

    long generator = Integer.parseInt(generatorCandidates.get(0), 2);
    long scrubber = Integer.parseInt(scrubberCandidates.get(0), 2);

    System.out.println("Part 2: " + (generator * scrubber));
  }
}
