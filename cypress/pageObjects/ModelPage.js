class ModelPage {
    visit() {
      cy.visit("http://127.0.0.1:8001");
    }
  
    enterModelName(name) {
        cy.get('#text_input_1').type(name);
    }
  
    submitModel() {
        cy.contains("Train Model").click();
    }
  
    verifyModelInList() {
        cy.contains("PROCESSING").should("be.visible");
    }
  
    verifyErrorMessage(message) {
      cy.contains(message).should("be.visible");
    }

  }
  
  export default ModelPage;
  