import os
import wx
import wx.xrc
import wx.grid
import sqlite3
import re
import string
import gettext


cwd = os.path.abspath(os.curdir)

def connect():
        con_str = cwd + '/folder/Test.db'
        cnn = sqlite3.connect(con_str)
        return cnn
        cnn.close()

def data_rows():
        con = connect()
        cur = con.cursor()
        cur.execute("SELECT * FROM DATA")
        rows = cur.fetchall()
        i = 0
        for r in rows:
                i+= 1
        return i

def single_quote_remover(text):
    return text.replace ("'","/")


class Database ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Databease Management", pos = wx.DefaultPosition, size = wx.Size( 800,447 ), style = wx.DEFAULT_FRAME_STYLE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour(wx.Colour(52,203,142))
        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Welcome To Database System", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.m_staticText1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )

        bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size(20,20), wx.TAB_TRAVERSAL )
        self.m_panel1.SetBackgroundColour(wx.Colour(52,203,142))
        bSizer16.Add( self.m_panel1, 1, wx.ALL, 5 )


        bSizer7.Add( bSizer16, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"             ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer11.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.txtID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 180,-1 ), 0 )
        self.txtID.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.txtID.Enabled = False
        bSizer11.Add( self.txtID, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer7.Add( bSizer11, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"      Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer12.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.txtName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.txtName.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.txtName.Enabled = False
        bSizer12.Add( self.txtName, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer7.Add( bSizer12, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"         Age :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer13.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.txtAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.txtAge.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.txtAge.Enabled = False
        bSizer13.Add( self.txtAge, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer7.Add( bSizer13, 1, wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Address : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer14.Add( self.m_staticText6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.txtAddress = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
        self.txtAddress.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.txtAddress.Enabled = False
        bSizer14.Add( self.txtAddress, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer7.Add( bSizer14, 1, wx.EXPAND, 5 )

        bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnAdd = wx.Button( self, wx.ID_ANY, u"Add New", wx.DefaultPosition, wx.Size( 100,28 ), 0 )
        self.btnAdd.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.btnAdd.SetBackgroundColour( wx.Colour(178,178,178) )

        bSizer15.Add( self.btnAdd, 0, wx.ALL, 5 )

        self.btnSave = wx.Button( self, wx.ID_ANY, u"Save/Update", wx.DefaultPosition, wx.Size( 100,28 ), 0 )
        self.btnSave.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.btnSave.SetBackgroundColour( wx.Colour(178,178,178) )

        bSizer15.Add( self.btnSave, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer15, 1, wx.ALIGN_RIGHT, 5 )


        bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Search by name :", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer9.Add( self.m_staticText2, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

        self.txtSearch = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
        self.txtSearch.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

        bSizer9.Add( self.txtSearch, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

        self.btnSearch = wx.Button( self, wx.ID_ANY, u"Search", wx.DefaultPosition, wx.Size( 100,28 ), 0 )
        self.btnSearch.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.btnSearch.SetBackgroundColour(wx.Colour(178,178,178))

        bSizer9.Add( self.btnSearch, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )


        bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,195 ), 0 )

        # Grid
        self.m_grid1.CreateGrid( 10, 4 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelSize( 30 )
        self.m_grid1.SetColLabelValue( 0, u"ID" )
        self.m_grid1.SetColLabelValue( 1, u"Name" )
        self.m_grid1.SetColLabelValue( 2, u"Age" )
        self.m_grid1.SetColLabelValue( 3, u"Address" )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelSize( 80 )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        self.m_grid1.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

        bSizer8.Add( self.m_grid1, 0, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.btnDelete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.Size( 100,28 ), 0 )
        self.btnDelete.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.btnDelete.SetBackgroundColour( wx.Colour(178,178,178) )

        bSizer10.Add( self.btnDelete, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.btnExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( 100,28 ), 0 )
        self.btnExit.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.btnExit.SetBackgroundColour( wx.Colour(178,178,178) )

        bSizer10.Add( self.btnExit, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.btnLoad = wx.Button( self, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.Size( 100,28 ), 0 )
        self.btnLoad.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )
        self.btnLoad.SetBackgroundColour( wx.Colour(178,178,178) )

        bSizer10.Add( self.btnLoad, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer8.Add( bSizer10, 1, wx.EXPAND, 5 )


        bSizer6.Add( bSizer8, 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )


        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )

        self.refresh_data()

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btnAdd.Bind( wx.EVT_BUTTON, self.btnAddClick )
        self.btnAdd.Bind( wx.EVT_ENTER_WINDOW, self.addMouseEnter )
        self.btnAdd.Bind( wx.EVT_LEAVE_WINDOW, self.addMouseExit )
        self.btnSave.Bind( wx.EVT_BUTTON, self.btnSaveClick )
        self.btnSave.Bind( wx.EVT_ENTER_WINDOW, self.saveMouseEnter )
        self.btnSave.Bind( wx.EVT_LEAVE_WINDOW, self.saveMouseExit )
        self.btnSearch.Bind( wx.EVT_BUTTON, self.btnSearchClick )
        self.btnSearch.Bind( wx.EVT_ENTER_WINDOW, self.searchMouseEnter )
        self.btnSearch.Bind( wx.EVT_LEAVE_WINDOW, self.searchMouseExit )
        self.btnDelete.Bind( wx.EVT_BUTTON, self.btnDeleteClick )
        self.btnDelete.Bind( wx.EVT_ENTER_WINDOW, self.deleteMouseEnter )
        self.btnDelete.Bind( wx.EVT_LEAVE_WINDOW, self.deleteMouseExit )
        self.btnExit.Bind( wx.EVT_BUTTON, self.btnExitClick )
        self.btnExit.Bind( wx.EVT_ENTER_WINDOW, self.exitMouseEnter )
        self.btnExit.Bind( wx.EVT_LEAVE_WINDOW, self.exitMouseExit )

        self.btnLoad.Bind( wx.EVT_BUTTON, self.btnLoadClick )
        self.btnLoad.Bind( wx.EVT_ENTER_WINDOW, self.loadMouseEnter )
        self.btnLoad.Bind( wx.EVT_LEAVE_WINDOW, self.loadMouseExit )

    def __del__( self ):
        pass



    def refresh_data(self):
        cnn = connect()
        cur = cnn.cursor()
        cur.execute("SELECT * FROM DATA")
        rows = cur.fetchall()

        for i in range(0,len(rows)):
            for j in range(0,4):
                cell = rows[i]
                self.m_grid1.SetCellValue(i,j,str(cell[j]))

    def clear_grid(self):
        self.txtID.Value=""
        self.txtName.Value=""
        self.txtAge.Value=""
        self.txtAddress.Value=""

    # Virtual event handlers, overide them in your derived class
    def btnAddClick( self, event ):
        self.txtID.Enabled = True
        self.txtName.Enabled = True
        self.txtAge.Enabled = True
        self.txtAddress.Enabled = True
        event.Skip()


    def addMouseEnter( self, event ):
        self.btnAdd.SetBackgroundColour( wx.Colour(255,0,128) )
        event.Skip()

    def addMouseExit( self, event ):
        self.btnAdd.SetBackgroundColour( wx.Colour(178,178,178) )
        event.Skip()

    def btnSaveClick( self, event ):
        if self.txtID.Value == "" or self.txtName.Value == "" or self.txtAge.Value == "" or self.txtAddress.Value == "":
            wx.MessageBox("Please Insert Information!")
        else:
            the_id=str(self.txtID.Value)
            the_name=single_quote_remover(str(self.txtName.Value))
            the_age=single_quote_remover(str(self.txtAge.Value))
            the_address=single_quote_remover(str(self.txtAddress.Value))
            self.m_grid1.AppendRows(1)
            cnn = connect()
            cursor = cnn.cursor()
            add_many = "INSERT INTO DATA(ID,Name,Age,Address) VALUES("+(the_id)+",'"+(the_name)+"','"+(the_age)+"','"+(the_address)+"')"
            cursor.execute(add_many)
            cnn.commit()
            cnn.close()
            self.refresh_data()
            self.clear_grid()
            self.txtName.SetFocus()
        event.Skip()

    def saveMouseEnter( self, event ):
        self.btnSave.SetBackgroundColour( wx.Colour(255,0,128) )
        event.Skip()

    def saveMouseExit( self, event ):
        self.btnSave.SetBackgroundColour( wx.Colour(178,178,178) )
        event.Skip()

    def btnSearchClick( self, event ):
        r=data_rows()
        for e in range(0,r):
            for f in range(0,4):
                self.m_grid1.SetCellValue(e,f,"")
        cnn=connect()
        cursor=cnn.cursor()
        cursor.execute("SELECT * FROM DATA WHERE Name LIKE '%"+self.txtSearch.Value+"%'")
        cnn.commit()
        rows=cursor.fetchall()
        for i in range(len(rows)):
            for j in range(0,4):
                cell=rows[i]
                self.m_grid1.SetCellValue(i,j,str(cell[j]))
        cnn.close()
        self.txtSearch.SetFocus()
        event.Skip()


    def searchMouseEnter( self, event ):
        self.btnSearch.SetBackgroundColour( wx.Colour(255,0,128) )
        event.Skip()

    def searchMouseExit( self, event ):
        self.btnSearch.SetBackgroundColour( wx.Colour(178,178,178) )
        event.Skip()

    def btnDeleteClick( self, event ):
        try:
            lst = self.m_grid1.GetSelectedRows()[0]
            c=self.m_grid1.GetCellValue(lst,0)
            cnn=connect()
            cur=cnn.cursor()
            cur.execute("DELETE FROM DATA WHERE ID="+"'" + str(c) + "'")
            cnn.commit()
            cnn.close()
            self.m_grid1.DeleteRows(lst,1)
            self.refresh_data()
            self.txtName.SetFocus()
        except IndexError:
            wx.MessageBox("You Did Not Select Any Row To Delete!")
        event.Skip()


    def deleteMouseEnter( self, event ):
        self.btnDelete.SetBackgroundColour( wx.Colour(255,0,128) )
        event.Skip()

    def deleteMouseExit( self, event ):
        self.btnDelete.SetBackgroundColour( wx.Colour(178,178,178) )
        event.Skip()

    def btnExitClick( self, event ):
        self.Destroy()
        event.Skip()


    def exitMouseEnter( self, event ):
        self.btnExit.SetBackgroundColour( wx.Colour(255,0,128) )
        event.Skip()

    def exitMouseExit( self, event ):
        self.btnExit.SetBackgroundColour( wx.Colour(178,178,178) )
        event.Skip()


    def btnLoadClick( self, event ):
            cnn = connect()
            cur = cnn.cursor()
            cur.execute("SELECT * FROM DATA")
            rows = cur.fetchall()

            for i in range(0,len(rows)):

                    for j in range(0,4):
                            cell = rows[i]
                            self.m_grid1.SetCellValue(i,j,str(cell[j]))


    def loadMouseEnter( self, event ):
        self.btnLoad.SetBackgroundColour( wx.Colour(255,0,128) )
        event.Skip()

    def loadMouseExit( self, event ):
        self.btnLoad.SetBackgroundColour( wx.Colour(178,178,178) )
        event.Skip()



app = wx.App(False)
frame = Database(None)
frame.Show()
app.MainLoop()
