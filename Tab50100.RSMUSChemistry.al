table 50100 "Chemistry"
{
    DataClassification = ToBeClassified;

    fields
    {
        field(1; Element; Text[50])
        {
            DataClassification = ToBeClassified;
            Caption = 'Element';
        }
        field(2; Symbol; Text[50])
        {
            DataClassification = ToBeClassified;
            Caption = 'Symbol';
        }
        field(3; "Atomic_Number"; Integer)
        {
            DataClassification = ToBeClassified;
            Caption = 'Atomic_Number';
        }
        field(4; "Atomic_Weight"; Text[50])
        {
            DataClassification = ToBeClassified;
            Caption = 'Weight';
        }
        field(5; Group; Integer)
        {
            DataClassification = ToBeClassified;
            Caption = 'Element_Group';
        }
        field(6; Period; Integer)
        {
            DataClassification = ToBeClassified;
            Caption = 'Period';
        }
        field(7; Property; Text[50])
        {
            DataClassification = ToBeClassified;
            Caption = 'Property';
        }
    }

    keys
    {
        key(PK; "Element")
        {
            Clustered = true;
        }
    }
}