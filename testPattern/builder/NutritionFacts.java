
/**
 * Builder 模式
 * 当类的参数过多时，构造函数的组合就非常繁杂，这时设置一个静态内部类（Builder），
 * 在 Builder 中对每个参数都设置一个对应的方法，且方法返回 Builder 原 builder 对象，这样就可以写成一串，
 * 最终通过一个 build() 方法返回一个构造好的对象
 */
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;

    public static class Builder {
        private final int servingSize;
        private final int servings;

        private int calories        = 0;
        private int fat             = 0;
        private int carbohydrate    = 0;
        private int sodium          = 0;

        public Builder(int servingSize, int servings){
            this.servingSize = servingSize;
            this.servings = servings;
        }

        public Builder calories(int val){
            this.calories = val;
            return this;
        }
        public Builder fat(int val){
            this.fat = val;
            return this;
        }
        public Builder carbohydrate(int val){
            this.carbohydrate = val;
            return this;
        }
        public Builder sodium(int val){
            this.sodium = val;
            return this;
        }
        public NutritionFacts build(){
            return new NutritionFacts(this);
        }
    }

    private NutritionFacts(Builder builder){
        this.servingSize  = builder.servingSize;
        this.servings     = builder.servings;
        this.calories     = builder.calories;
        this.fat          = builder.fat;
        this.sodium       = builder.sodium;
        this.carbohydrate = builder.carbohydrate;
    }

    public int getCalories(){
        return calories;
    }

    public static void main(String[] args){
        NutritionFacts cocaCola = new NutritionFacts.Builder(240,8)
                .calories(100)
                .sodium(35)
                .carbohydrate(27)
                .build();
        System.out.println(cocaCola.getCalories());
    }
}
