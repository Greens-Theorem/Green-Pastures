/**
 * @author Cowen Hames January 2021
 * This is the UI of the train database. This class inherits the information from the database class then uses GUI to display the information to the user.
 */
package database;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;

public class Train_UI extends Train_DB implements ActionListener {

	// frame
	JFrame f;
	// Table
	JTable j;

	// Constructor
	Train_UI() {

		JFrame frame = new JFrame("Train Information System");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(300, 300);
		JTextField dataOutput = new JTextField("", 5000);
		JButton button1 = new JButton("Train Information");
		frame.add(button1, BorderLayout.NORTH);
		JButton button2 = new JButton("Station Information");
		frame.add(button2, BorderLayout.SOUTH);
		frame.setVisible(true);
		button1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent evt) {
				// delegate to event handler method
				actionPerformed(evt);
			}
		});
	}

	@Override
	public void actionPerformed(ActionEvent e) {

	}

	public static void main(String[] args) {
		new Train_UI();
	}
}