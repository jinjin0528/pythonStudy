import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rowNum = sc.nextInt();
        int colNum = sc.nextInt();
        int num = 1;
        for(int i = 0; i < rowNum; i++){
            for(int j = 0; j<colNum; j++) {
                System.out.print(num);
            } System.out.println();
        }
    }
}