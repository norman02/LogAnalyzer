# **LogFusion**  
A lightweight Python-based log analyzer for IT support professionals.

## **Overview**  
LogFusion is designed to streamline log analysis by parsing system, application, and network logs, categorizing issues, and providing structured JSON reports. It's built with flexibility in mind, ensuring compatibility across various log formats.

## **Features**  
✅ Parses logs using regex and structured rules  
✅ Categorizes errors, warnings, and informational logs  
✅ Stores processed logs in JSON format for easy integration  
✅ Supports multiple log sources (system, application, network)  
✅ Optimized for performance with large log files  
✅ Open-source and lightweight—no external dependencies required  

## **Project Roadmap**  
### **Phase 1: Initial Setup**  
- [x] Define core objectives and scope  
- [ ] Establish project structure (`log_analyzer/`)  
- [ ] Develop a basic log ingestion script (`parser.py`)  

### **Phase 2: Core Log Analysis**  
- [ ] Implement regex-based log parsing  
- [ ] Categorize logs into errors, warnings, and info  
- [ ] Export structured logs in JSON format (`reporter.py`)  
- [ ] Add unit tests to ensure reliability  

### **Phase 3: Advanced Features**  
- [ ] Introduce severity tagging for critical issues  
- [ ] Enable multi-log source support  
- [ ] Implement alert system for high-impact errors  
- [ ] Optimize performance for handling large logs  

### **Phase 4: Documentation & Refinements**  
- [ ] Improve documentation with usage examples  
- [ ] Add configuration options (`config.json`)  
- [ ] Refactor code for efficiency and modularity  
- [ ] Gather community feedback for refinements  

### **Phase 5: Future Enhancements**  
- [ ] Explore machine learning for log anomaly detection  
- [ ] Consider integrations with IT automation tools  
- [ ] Develop a lightweight web interface (if needed)  
- [ ] Expand compatibility with more log formats  

## **Installation & Usage**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/LogFusion.git
   cd LogFusion
   ```
2. Install dependencies (if any):  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the log analyzer on sample logs:  
   ```bash
   python src/parser.py logs/sample_log.txt
   ```

## **License**  
This project is licensed under the **MIT License**—open for contributions and modifications.  

