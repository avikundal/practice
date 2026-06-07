public class practice{
    public static void main(String[] args)
    {
        String h = "Hello", w = "World";
        System.out.println("Hello, World");
        System.out.println(h + " " +  w);
    }

}


class Employee{
    String name;
    String[] projects;

    Employee(String name, String[] projects){
        this.name = name;
        this.projects = projects;
    }

    Employee(Employee e){
        this.name = e.name;
        this.projects = e.projects;
    }
}



import java.util.Scanner;
class Faculty{
   private String name;
   private double salary;
   public Faculty(String name, double salary) {
       this.name = name;
       this.salary = salary;
   }
   public double bonus(float percent){
       return (percent/100.0)*salary;
   }
   public static getDetails{

   }
   // Define method getDetails()
    // Override method getDetails(float percent)
}
class Hod extends Faculty{
    private String personalAssistant;
    public Hod(String name, double salary, String pa) {
        super(name, salary);
        this.personalAssistant = pa;
    }
    // Override method bonus(float percent)
    // Override method getDetails()
    // Override method getDetails(float percent)
}
public class InheritanceTest{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        Faculty obj1 = new Faculty(sc.next(), sc.nextDouble());
        Faculty obj2 = new Hod(sc.next(), sc.nextDouble(), sc.next());
        System.out.println(obj1.getDetails());
        System.out.println(obj1.getDetails(10));
        System.out.println(obj2.getDetails());
        System.out.println(obj2.getDetails(10));
    }
}





for(int i = 0; i < sList.size(); i++){
    Shop s = sList.get(i);

    String name = s.getName();
    int count = s.getItemSold();

    m.put(name, count);

    if(count > sold){
        sold = count;
        shop = name;
    }
}





for (int i =0; i < )