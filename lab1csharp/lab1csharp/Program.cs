using System;

class BiquadraticEquation
{
    private double a;
    private double b;
    private double c;
    
    public BiquadraticEquation(double a=0, double b=0, double c=0)
    {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    
    private double CalculateDiscriminant()
    {
        return b * b - 4 * a * c;
    }
    
    public void Solve()
    {
        if (a == 0)
        {
            Console.WriteLine("Это не биквадратное уравнение, коэффициент a не может быть равен 0.");
            return;
        }
        
        double discriminant = CalculateDiscriminant();
        Console.WriteLine($"Дискриминант: {discriminant}");

        if (discriminant < 0)
        {
            Console.WriteLine("Корней нет, дискриминант меньше нуля.");
        }
        else
        {
            double y1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
            double y2 = (-b - Math.Sqrt(discriminant)) / (2 * a);
            
            SolveForX(y1);
            SolveForX(y2);
        }
    }
    
    private void SolveForX(double y)
    {
        if (y < 0)
        {
            Console.WriteLine($"Корней для y = {y} нет, так как x^2 = y не может иметь отрицательное значение.");
        }
        else if (y == 0)
        {
            Console.WriteLine($"Корень x = 0 для y = {y}");
        }
        else
        {
            double x1 = Math.Sqrt(y);
            double x2 = -Math.Sqrt(y);
            Console.WriteLine($"Корни для y = {y}: x1 = {x1}, x2 = {x2}");
        }
    }

    public void GetCoefficients()
    {
        Console.Write("Введите коэффициент a: ");
        this.a = Convert.ToDouble(Console.ReadLine());
        Console.Write("Введите коэффициент b: ");
        this.b = Convert.ToDouble(Console.ReadLine());
        Console.Write("Введите коэффициент c: ");
        this.c = Convert.ToDouble(Console.ReadLine());
    }
}

class Program
{
    static void Main()
    {
        BiquadraticEquation equation = new BiquadraticEquation();
        equation.GetCoefficients();
        equation.Solve();
    }
}