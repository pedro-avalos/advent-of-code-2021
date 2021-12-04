import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Consumption.
 *
 * @author Pedro Avalos
 */
public class Consumption {

  /**
   * Input data split into numbers represented as text.
   */
  private List<String> report;

  /**
   * Length of each number in the input.
   */
  private int numberLength;

  /**
   * Text representaion of the gamma rate, in binary.
   */
  private String gamma;

  /**
   * Text representaion of the epsilon rate, in binary.
   */
  private String epsilon;

  /**
   * Text representaion of the generator rating, in binary.
   */
  private String generator;

  /**
   * Text representaion of the scrubber rating, in binary.
   */
  private String scrubber;

  /**
   * Constructor.
   * 
   * @param fileName Name of the input file.
   */
  public Consumption(String fileName) {
    File file = new File(fileName);
    Scanner scanner = null;
    try {
      scanner = new Scanner(file);
    } catch (FileNotFoundException e) {
      System.out.println("File '" + fileName + "' not found.");
      System.exit(1);
    }

    report = new ArrayList<>();
    while (scanner.hasNextLine())
      report.add(scanner.nextLine().strip());
    scanner.close();

    numberLength = report.get(0).length();
    gamma = new String();
    epsilon = new String();
    generator = new String();
    scrubber = new String();
  }

  /**
   * Calculate the gamma and epsilon rates. This is part 1 of the challenge.
   */
  public void calculateRates() {
    for (int i = 0; i < numberLength; i++) {
      int countOnes = 0;

      for (String num : report)
        try {
          countOnes += Integer.parseInt("" + num.charAt(i));
        } catch (NumberFormatException e) {
          System.out.println("Noninteger input '" + num + "'.");
          System.exit(1);
        }

      gamma += (2 * countOnes >= report.size()) ? "1" : "0";
      epsilon += (2 * countOnes < report.size()) ? "1" : "0";
    }
  }

  /**
   * Calculate the generator and scrubber ratings. This is part 2 of the
   * challenge.
   */
  public void calculateRatings() {
    ArrayList<String> generatorCandidates = new ArrayList<>(report);
    ArrayList<String> scrubberCandidates = new ArrayList<>(report);

    for (int charPos = 0; generatorCandidates.size() > 1; charPos++) {
      int countOnes = 0;
      for (String s : generatorCandidates)
        countOnes += Integer.parseInt("" + s.charAt(charPos));
      char majority = (2 * countOnes >= generatorCandidates.size()) ? '1' : '0';

      for (int i = 0; i < generatorCandidates.size(); i++)
        if (generatorCandidates.get(i).charAt(charPos) != majority)
          generatorCandidates.remove(i--);
    }

    for (int charPos = 0; scrubberCandidates.size() > 1; charPos++) {
      int countOnes = 0;
      for (String s : scrubberCandidates)
        countOnes += Integer.parseInt("" + s.charAt(charPos));
      char minority = (2 * countOnes < scrubberCandidates.size()) ? '1' : '0';

      for (int i = 0; i < scrubberCandidates.size(); i++)
        if (scrubberCandidates.get(i).charAt(charPos) != minority)
          scrubberCandidates.remove(i--);
    }

    generator = generatorCandidates.get(0);
    scrubber = scrubberCandidates.get(0);
  }

  /**
   * Retrieve the gamma rate as a number.
   * 
   * @return Gamma rate.
   */
  public long getGamma() {
    return Integer.parseInt(gamma, 2);
  }

  /**
   * Retrieve the epsilon rate as a number.
   * 
   * @return Epsilon rate.
   */
  public long getEpsilon() {
    return Integer.parseInt(epsilon, 2);
  }

  /**
   * Retrieve the oxygen generator rating as a number.
   * 
   * @return Oxygen generator rating.
   */
  public long getGenerator() {
    return Integer.parseInt(generator, 2);
  }

  /**
   * Retrieve the CO2 scrubber rating as a number.
   * 
   * @return CO2 scrubber rating.
   */
  public long getScrubber() {
    return Integer.parseInt(scrubber, 2);
  }

  public static void main(String[] args) {
    Consumption consumption = new Consumption(
        args.length > 0 ? args[0] : "input.txt");

    consumption.calculateRates();
    consumption.calculateRatings();

    System.out.println(
        "Part 1: " + (consumption.getGamma() * consumption.getEpsilon()));
    System.out.println(
        "Part 2: " + (consumption.getGenerator() * consumption.getScrubber()));
  }
}
