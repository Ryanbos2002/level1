<grip:Pipeline>
  <sources>
    <grip:MultiImageFile>
      <property name="numImages" value="5"/>
      <property name="path[0]" value="/Users/s789927/Desktop/Grip_images/drive-download-20170926T214109Z-001/10.png"/>
      <property name="path[1]" value="/Users/s789927/Desktop/Grip_images/drive-download-20170926T214109Z-001/174.png"/>
      <property name="index" value="3"/>
      <property name="path[2]" value="/Users/s789927/Desktop/Grip_images/drive-download-20170926T214109Z-001/580.png"/>
      <property name="path[3]" value="/Users/s789927/Desktop/Grip_images/drive-download-20170926T214109Z-001/1140.png"/>
      <property name="path[4]" value="/Users/s789927/Desktop/Grip_images/drive-download-20170926T214109Z-001/1376.png"/>
    </grip:MultiImageFile>
  </sources>
  <steps>
    <grip:Step name="Resize Image">
      <grip:Input step="0" socket="0"/>
      <grip:Input step="0" socket="1">
        <value>605.0</value>
      </grip:Input>
      <grip:Input step="0" socket="2">
        <value>475.0</value>
      </grip:Input>
      <grip:Input step="0" socket="3">
        <value>LINEAR</value>
      </grip:Input>
      <grip:Output step="0" socket="0" previewed="false"/>
    </grip:Step>
    <grip:Step name="Blur">
      <grip:Input step="1" socket="0"/>
      <grip:Input step="1" socket="1">
        <value>BOX</value>
      </grip:Input>
      <grip:Input step="1" socket="2">
        <value>0.0</value>
      </grip:Input>
      <grip:Output step="1" socket="0" previewed="true"/>
    </grip:Step>
    <grip:Step name="HSL Threshold">
      <grip:Input step="2" socket="0"/>
      <grip:Input step="2" socket="1">
        <value>
          <double>58.27338129496402</double>
          <double>89.8471986417657</double>
        </value>
      </grip:Input>
      <grip:Input step="2" socket="2">
        <value>
          <double>117.77877697841726</double>
          <double>255.0</double>
        </value>
      </grip:Input>
      <grip:Input step="2" socket="3">
        <value>
          <double>68.79496402877697</double>
          <double>255.0</double>
        </value>
      </grip:Input>
      <grip:Output step="2" socket="0" previewed="true"/>
    </grip:Step>
  </steps>
  <connections>
    <grip:Connection>
      <grip:Output source="0" socket="0" previewed="false"/>
      <grip:Input step="0" socket="0"/>
    </grip:Connection>
    <grip:Connection>
      <grip:Output step="1" socket="0" previewed="true"/>
      <grip:Input step="2" socket="0"/>
    </grip:Connection>
    <grip:Connection>
      <grip:Output step="0" socket="0" previewed="false"/>
      <grip:Input step="1" socket="0"/>
    </grip:Connection>
  </connections>
  <settings>
    <teamNumber>0</teamNumber>
    <publishAddress>roboRIO-0-FRC.local</publishAddress>
    <deployAddress>roboRIO-0-FRC.local</deployAddress>
    <deployDir>/home/lvuser</deployDir>
    <deployUser>lvuser</deployUser>
    <deployJavaHome>/usr/local/frc/JRE/</deployJavaHome>
    <deployJvmOptions>-Xmx50m -XX:-OmitStackTraceInFastThrow -XX:+HeapDumpOnOutOfMemoryError -XX:MaxNewSize=16m</deployJvmOptions>
  </settings>
  <codeGenerationSettings>
    <language>Python</language>
    <className>GripPipeline</className>
    <implementWpilibPipeline>false</implementWpilibPipeline>
    <saveDir>/Users/s789927/Desktop</saveDir>
    <packageName></packageName>
    <moduleName>grip</moduleName>
  </codeGenerationSettings>
</grip:Pipeline>