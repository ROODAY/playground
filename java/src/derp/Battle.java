package derp;

public class Battle {
	Zach fighter1;
	Zach fighter2;

	public Battle(Zach one, Zach two) {
		this.fighter1 = one;
		this.fighter2 = two;
	}

	public Zach loganQuestion() {
		System.out.println(String.format("The fighters are %s and %s.", fighter1.nomen, fighter2.nomen));
		Random rand = new Random();
		while (fighter1.health > 0 && fighter2.health > 0) {
			int fighter = rand.nextInt(1);
			if (fighter == 0) {
				fighter2.health -= fighter1.damage;
			} else {
				fighter1.health -= fighter2.damage;
			}
		}
	}
}
