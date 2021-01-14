/*
 * @author Cowen Hames January 2021
 */
package database;

import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;

/*
 * The following class creates two databases for a Train Information System. The first database is for the trains themselves, and the second
 * is for the station. These two databases are then used in the UI class that inherits this class. This information is not allowed to be edited by the user.
 */

public class Train_DB {

	public static void main(String[] args) throws IOException, SQLException, ClassNotFoundException {

		SimpleDataSource.init("database.properties");

		try (Connection conn = SimpleDataSource.getConnection(); Statement stat = conn.createStatement()) {
			try {
				stat.execute("DROP TABLE Train_Database");
				stat.execute("DROP TABLE Station_Database");
			} catch (SQLException e) {
				// get exception if table doesn't exist yet
			}
			stat.execute(
					"CREATE TABLE Train_Database (Train_Num VARCHAR(20), Train_Name VARCHAR(30), Train_City VARCHAR(30), Train_Route VARCHAR(20), Train_Service_Type VARCHAR(30), Train_Day_Schedule VARCHAR(30))");
			stat.execute(
					"CREATE TABLE Station_Database (Station_Name VARCHAR(30), Station_Location VARCHAR(30), Station_Code_Number VARCHAR(30), Station_Train_Num VARCHAR(20))");

			// Headers for each table
			String header_train_db = "INSERT INTO Train_Database(Train_Num, Train_Name, Train_City, Train_Route, Train_Service_Type, Train_Day_Schedule) VALUES(?,?,?,?,?,?)";
			java.sql.PreparedStatement htd = conn.prepareStatement(header_train_db);
			htd.setString(1, "Train Number");
			htd.setString(2, "Train Name");
			htd.setString(3, "Train City");
			htd.setString(4, "Train Route");
			htd.setString(5, "Train Service Type");
			htd.setString(6, "Train Daily Schedule");
			htd.executeUpdate();

			String header_station_db = "INSERT INTO Station_Database(Station_Name, Station_Location, Station_Code_Number, Station_Train_Num) VALUES(?,?,?,?)";
			java.sql.PreparedStatement htd2 = conn.prepareStatement(header_station_db);
			htd2.setString(1, "Station Name");
			htd2.setString(2, "Station Location");
			htd2.setString(3, "Station Code Number");
			htd2.setString(4, "Station Train Number");
			htd2.executeUpdate();
			// Data Entry

			String sql = "INSERT INTO Train_Database(Train_Num, Train_Name, Train_City, Train_Route, Train_Service_Type, Train_Day_Schedule) VALUES(?,?,?,?,?,?)";
			java.sql.PreparedStatement s = conn.prepareStatement(sql);
			s.setString(1, "1001");
			s.setString(2, "Union Pacific");
			s.setString(3, "Chicago");
			s.setString(4, "WestBound");
			s.setString(5, "Freight");
			s.setString(6, "MTWRF");
			s.executeUpdate();

			String sql2 = "INSERT INTO Train_Database(Train_Num, Train_Name, Train_City, Train_Route, Train_Service_Type, Train_Day_Schedule) VALUES(?,?,?,?,?,?)";
			java.sql.PreparedStatement s2 = conn.prepareStatement(sql2);
			s2.setString(1, "2009");
			s2.setString(2, "Canadian National");
			s2.setString(3, "Quebec");
			s2.setString(4, "Northwestern");
			s2.setString(5, "Freight");
			s2.setString(6, "WRFSS");
			s2.executeUpdate();

			String sql3 = "INSERT INTO Station_Database(Station_Name, Station_Location, Station_Code_Number, Station_Train_Num) VALUES(?,?,?,?)";
			java.sql.PreparedStatement s3 = conn.prepareStatement(sql3);
			s3.setString(1, "UP_DavenPort_Iowa");
			s3.setString(2, "Davenport, Iowa");
			s3.setString(3, "900015");
			s3.setString(4, "1001");
			s3.executeUpdate();

			String sql4 = "INSERT INTO Station_Database(Station_Name, Station_Location, Station_Code_Number, Station_Train_Num) VALUES(?,?,?,?)";
			java.sql.PreparedStatement s4 = conn.prepareStatement(sql4);
			s4.setString(1, "CN_Fargo_ND");
			s4.setString(2, "Fargo, North Dakota");
			s4.setString(3, "400700");
			s4.setString(4, "2009");
			s4.executeUpdate();
			
		}

	}
}