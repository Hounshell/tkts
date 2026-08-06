package hounshell.tkts;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CalculatorTest {

    @Test
    void testAdd() {
        assertEquals(5, Calculator.add(2, 3));
        assertEquals(0, Calculator.add(-1, 1));
    }
}

