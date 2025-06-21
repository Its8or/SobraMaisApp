module its8or.com.sobramaisapp {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires eu.hansolo.tilesfx;

    opens its8or.com.sobramaisapp to javafx.fxml;
    exports its8or.com.sobramaisapp;
}