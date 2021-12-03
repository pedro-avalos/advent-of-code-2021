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
      System.out.println("File " + name + " not found.");
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
      int count = 0; // Count of 1s in the current position

      for (String num : report) {
        try {
          count += Integer.parseInt("" + num.charAt(i));
        } catch (NumberFormatException e) {
          System.out.println("Noninteger input.");
          e.printStackTrace();
          System.exit(1);
        }
      }

      gammaBits += 2 * count > report.size() ? 1 : 0;
      epsilonBits += 2 * count < report.size() ? 1 : 0;
    }

    int gamma = Integer.parseInt(gammaBits, 2);
    int epsilon = Integer.parseInt(epsilonBits, 2);

    System.out.println(gamma);
    System.out.println(epsilon);
    System.out.println(gamma * epsilon);
  }
}
