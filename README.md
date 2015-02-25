SoundCloud Archive
---

---

####General Idea:

* I use SoundCloud every day (almost more than Spotify and iTunes combined) to listen to really cool independently produced sounds and music from all over the world.  SoundCloud is an amazing service, however, since it's all hosted online and has little to zero physical footprint it has some drawbacks.  First off, only "certain" tracks can actually be downloaded, this also has to be done with a physical button in the UI (which for hundreds of tracks takes forever) which also doesn't include ID3 tagging or even the highest bit-rate.  

* Tools like YouTube_DL can be used to archive SoundCloud, but they have to be directed at a target, which makes archiving large collections combersome and slow.  Sometimes, they don't know what to do with stream errors which can be annoying.  The biggest issue I've run into is when artists take down tracks I really liked, essentially removing them forever with no physical presence.

---

####What SC_Archive actually does:

* When provided with a User ID and API key, SC_Archive looks at all of a user's likes and playlists and dynamically archives everything at a set interval.  No longer, does one need to manually enter URL's into archiving scripts or manually organize media from SoundCloud.

---

####Dev. Goals:

1.	Automated organization of archived files
	* Ideally a system based from a main repository that displays via aliases (removes duplicate downloads) to streamline disk space required and filename mixups.

2.	Ability to backup archive to rSync target or Amazon S3 account

3.	Ability to stream with open source streaming platform
	* It would be cool if this could be implemented on Amazon AWS & S3

4.	Track log of changes to SoundCloud library and display playlists in order of tracks added (new -> old | old -> new) 
	* ID3 tagging of "date modified" somehow needs to be implemented