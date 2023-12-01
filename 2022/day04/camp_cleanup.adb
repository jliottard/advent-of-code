with Ada.Text_IO; use Ada.Text_IO;
with Ada.Containers; use Ada.Containers;
with Ada.Containers.Vectors;

procedure Camp_Cleanup is
    F : FileType;
    File_Name : constant String := "input.txt";
    V: Vector;

    function Parse_Line(Line: String) return Boolean
    begin

    end Parse_Line;

    function Is_Included(
        First_Lower: Integer;
        First_Upper: Integer;
        Second_Lower: Integer;
        Second_Upper: Interger;) return Boolean;
    begin
        if First_Lower <= Second_Lower and Second_Upper <= First_Lower or
            Second_Lower <= First_Lower and First_Lower <= Second_Upper then
            return True;
        else
            return False;
        end if;
    end Is_Included;
begin
    Open(F, In_File, File_Name);
    declare
        Value: Integer;
    while not End_Of_Life(F) loop
        Get_Line(F, value);
    end loop;
    Close(F);
end Camp_Cleanup;