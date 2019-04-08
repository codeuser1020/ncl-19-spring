import java.io.PrintStream;
import java.security.NoSuchAlgorithmException;

public class HashCode2
{
  public HashCode2() {}
  
  public static void main(String[] arr) throws java.io.IOException, NoSuchAlgorithmException
  {
    if (arr.length != 1) {
      System.out.println("Usage: java HashCode <tid>");
      System.exit(1);
    }

    byte[] arrayOfByte = arr[0].getBytes();
    int i = 0;
    for (int j = 0; j < arrayOfByte.length; j++) {
      i += (0xFE ^ arrayOfByte[j]) % 10000;
    }
    String str = "SKY-JDEC-" + String.format("%04d", new Object[] { Integer.valueOf(i) });
    System.out.println(str);
    System.out.println("The Java hashcode of the flag is: " + str.hashCode() + ". Good luck");
  }
}