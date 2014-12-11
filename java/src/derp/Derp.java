package derp;

public class Derp {

	public static void main(String[] args){
		Zach zach = new Zach(100, 10, "Zacharias");
		Zach zachary = new Zach(200, 5, "Zachathaniel");
		Battle verdun = new Battle(zach, zachary);
		verdun.loganQuestion();
	}

}