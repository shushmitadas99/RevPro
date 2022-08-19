package com.revature.main;

public class Driver {
    //Type in the shortcut 'main' and press ENTER to create the main method
    public static void main(String[] args) {
        System.out.println("Hello World!");
        dataTypeDemo();
    }

    public static void dataTypeDemo(){
        //Type in the shortcut 'sout' and press ENTER to create a print statement
        System.out.println("dataTypeDemo() works!");

        // Primitives
        boolean myBoolean; // Declaring (creating) a variable
        myBoolean = false; // Initialize the variable's value

        byte myByte = 10; // Declaring a variable and initializing its value on the same line
        short myShort = 2000;
        char myChar = '@'; // single quotes cannot be used for Strings in Java. They can only be used for chars
        // single quotes are "char literals"
        int myInt = 453422343;
        long myLong = 4342348409890L; // L at the end of the number indicates that it is a "long literal"
        float myFloat = 3.1415F; // F at the end of the number indicates it is a "float literal"
        double myDouble = 3.1415; // floating point numbers are doubles by default

        System.out.println(myBoolean);
        myBoolean = true; // re-assignment
        // notice we don't do boolean myBoolean = true, because myBoolean already exists. You only need to
        // declare a variable once with a particular type
        System.out.println(myBoolean);  // false;

        System.out.println(myByte); // 10
        System.out.println(myShort); //2000
        System.out.println(myChar);  // @
        System.out.println(myInt); // 453422343
        System.out.println(myLong);  // 4342348409890
        System.out.println(myFloat);
        System.out.println(myDouble);
    }
}
