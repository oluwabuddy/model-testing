import ModelPage from "../pageObjects/ModelPage";

describe("Model Training Workflow", () => {
  const modelPage = new ModelPage();

  beforeEach(() => {
    modelPage.visit();
  });

  it("should create a new model and display processing status", () => {
    modelPage.enterModelName("TestModel");
    modelPage.submitModel();
    modelPage.verifyModelInList("TestModel", "PROCESSING");
  });

  it("should update model status to SUCCESS", () => {
    modelPage.verifyModelInList("TestModel", "SUCCESS");
  });

  // it("should show an error for empty model name input", () => {
  //   modelPage.submitModel();
  //   modelPage.verifyErrorMessage("Model name is required");
  // });

  it("should add a new model entry to the list", () => {
    modelPage.enterModelName("NewModel");
    modelPage.submitModel();
    modelPage.verifyModelInList("NewModel", "PROCESSING");
  });

  it("should display FAILED status if model training fails", () => {
    modelPage.verifyModelInList("TestModel", "FAILED");
  });

});
