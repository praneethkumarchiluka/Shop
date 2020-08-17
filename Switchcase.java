public class Switchcase {
	
	boolean isweakday(int daynumber) {
		
		switch(daynumber)
		{
		case 1:
			return(true);
			
		case 2:
			return(false);
			
		case 3:
			return(false);
			
		case 4:
			return(false);
			
		case 5:
			return(false);
			
		case 6:
			return(false);
			
		case 7:
			return(true);
			
		defalut:
			return(false);
			break;
		}
		return false;
	}
}
class Case{
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Switchcase s=new Switchcase();
		s.isweakday(4);
	}

}
