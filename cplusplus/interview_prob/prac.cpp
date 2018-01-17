#include <iostream>
#include <string>
#include <ctype.h>


class TextInput
{
public:
    std::string text;
    TextInput() { text = ""; }
    
    virtual void add(char c) {
        text = text + c;
    }

    std::string getValue() { return text; }
};

class NumericInput : public TextInput {
public:
    void add(char c) {
        if(isdigit(c)){
            text = text + c;    
        }
    }
};

int main()
{
    TextInput* input = new NumericInput();
    input->add('1');
    input->add('a');
    input->add('0');
    std::cout << input->getValue();

    return 0;
}