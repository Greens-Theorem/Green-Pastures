page 50101 "RSMUSCarChallenge"
{
    PageType = List;
    ApplicationArea = All;
    UsageCategory = Lists;
    SourceTable = RSMUSCars;

    layout
    {
        area(Content)
        {
            repeater(Group)
            {
                field(Year; Rec.Year)
                {
                    ApplicationArea = All;

                }
                field(Make; Rec.Make)
                {
                    ApplicationArea = All;

                }
                field(Model; Rec.Model)
                {
                    ApplicationArea = All;

                }
                field(Trim; Rec.Trim)
                {
                    ApplicationArea = All;

                }
                field(Cylinders; Rec.Cylinders)
                {
                    ApplicationArea = All;

                }
                field(Displacement; Rec.Displacement)
                {
                    ApplicationArea = All;

                }
                field(HP; Rec.Torque)
                {
                    ApplicationArea = All;

                }
                field(MPG; Rec.MPG)
                {
                    ApplicationArea = All;

                }
                field(ManufactureDate; Rec.ManufactureDate)
                {
                    ApplicationArea = All;

                }
                field(Curbweight; Rec.CurbWeight)
                {
                    ApplicationArea = All;

                }
            }
        }
    }

    actions
    {
        area(Processing)
        {
            action(LoadData)
            {
                ApplicationArea = All;

                trigger OnAction()
                begin
                    LoadXML();
                end;
            }
        }
    }

    procedure LoadXML()
    var
        FileInStream: InStream;
        FileName: Text;
        CarLineImport: XmlPort RSMUSMyXmlport;
    begin
        UploadIntoStream('', '', '', FileName, FileInStream);
        CarLineImport.SetSource(FileInStream);
        CarLineImport.Import();

        Message('Upload successful');
    end;
}