page 50100 "RSMUSChemistry"
{
    PageType = List;
    ApplicationArea = All;
    SourceTable = Chemistry;
    UsageCategory = Lists;
    Caption = 'Chemistry';

    layout
    {
        area(Content)
        {
            repeater(Group)
            {
                field(Element; Rec.Element)
                {
                    ApplicationArea = All;

                }
                field(Symbol; Rec.Symbol)
                {
                    ApplicationArea = All;

                }
                field("Atomic_Number"; Rec.Atomic_Number)
                {
                    ApplicationArea = All;
                }

                field("Atomic_Weight"; Rec.Atomic_Weight)
                {
                    ApplicationArea = All;

                }
                field("Element_Group"; Rec.Group)
                {
                    ApplicationArea = All;
                }
                field(Period; Rec.Period)
                {
                    ApplicationArea = All;
                }
                field(Property; Rec.Property)
                {
                    ApplicationArea = All;
                }
            }
        }

    }

    actions
    {

    }
}