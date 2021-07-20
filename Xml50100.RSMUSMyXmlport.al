xmlport 50100 "RSMUSMyXmlport"
{
    Format = VariableText;
    schema
    {
        textelement(root)
        {
            tableelement(carline; RSMUSCars)
            {
                fieldattribute(Year; carline.Year)
                {

                }
                fieldattribute(Make; carline.Make)
                {

                }
                fieldattribute(Model; carline.Model)
                {

                }
                fieldattribute(Trim; carline.Trim)
                {

                }
                fieldattribute(Cylinders; carline.Cylinders)
                {

                }
                fieldattribute(Displacement; carline.Displacement)
                {
                }
                fieldattribute(HP; carline.HP)
                {

                }
                fieldattribute(Torque; carline.Torque)
                {

                }
                fieldattribute(MPG; carline.MPG)
                {

                }
                fieldattribute(ManufactureDate; carline.ManufactureDate)
                {

                }
                fieldattribute(Curbweight; carline.CurbWeight)
                {

                }
            }
        }
    }
}