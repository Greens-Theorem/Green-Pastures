table 50101 "RSMUSCars"
{
    DataClassification = ToBeClassified;

    fields
    {
        field(1; Year; Text[30])
        {
            DataClassification = ToBeClassified;

        }
        field(2; Make; Text[30])
        {
            DataClassification = ToBeClassified;

        }
        field(3; Model; Text[30])
        {
            DataClassification = ToBeClassified;

        }
        field(4; Trim; Text[30])
        {
            DataClassification = ToBeClassified;

        }
        field(5; Cylinders; Integer)
        {
            DataClassification = ToBeClassified;

        }
        field(6; Displacement; Decimal)
        {
            DataClassification = ToBeClassified;

        }
        field(7; HP; Integer)
        {
            DataClassification = ToBeClassified;

        }
        field(8; Torque; Integer)
        {
            DataClassification = ToBeClassified;

        }
        field(9; MPG; Integer)
        {
            DataClassification = ToBeClassified;

        }
        field(10; ManufactureDate; Date)
        {
            DataClassification = ToBeClassified;

        }
        field(11; CurbWeight; Integer)
        {
            DataClassification = ToBeClassified;

        }
    }

    keys
    {
        key(PK; ManufactureDate)
        {
            Clustered = true;
        }
    }
}